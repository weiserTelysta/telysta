// authHttp.ts 完整改进
import http from './http';

// 类型定义
interface LoginResponse {
  access_token: string;
  refresh_token: string;
  user: {
    uid: string;
    username: string;
    email: string;
  };
}

interface RegisterResponse {
  message: string;
  email: string;
}

interface ActivationResponse {
  message: string;
  code: string;
  user?: {
    email: string;
    username: string;
  };
}

interface ResendActivationPayload {
  email: string;
}

// API 方法
const authHttp = {
  // 登录
  login: (email: string, password: string) => {
    return http.post<LoginResponse>('/auth/login/', { email, password });
  },

  // 注册
  // authHttp.ts 注册方法
  register: async (email: string, username: string, password: string) => {
    const res = await http.post<RegisterResponse>('/auth/register/', {
      email,
      username,
      password
    });
    localStorage.setItem('pending_email', email); // 新增
    return res;
  },

  // 激活账户
  activate: (token: string) => {
    return http.get<ActivationResponse>(`/auth/activate/${token}/`);
  },

  // 重新发送激活邮件
  resendActivation: (email: string) => {
    return http.post<void>('/auth/resend_activation/', { email });
  },

  // 检查用户名可用性
  checkUsername: (username: string) => {
    return http.get<{ available: boolean }>(
      `/auth/check_username/?username=${encodeURIComponent(username)}`
    );
  }
};

export default authHttp;