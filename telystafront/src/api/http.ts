import axios from 'axios'

const service = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL,
    timeout:10000
});

service.interceptors.request.use(
    config => {
        if (config.url && !config.url.includes('/auth/')) {
            const token = localStorage.getItem('token');
            if (token) {
                config.headers.Authorization = `Bearer ${token}`;
            }
        }
        return config;
    },
    error => Promise.reject(error)
);

service.interceptors.response.use(
    response => {
        return response.data;
    },
    error =>{
        const status = error.resonse?.status;
        let message = error.message;

        switch(status){
            case 401:
                message = "身份验证失败";
                break;
        }
        return Promise.reject({status,message})
    }
);

const http = {
    get: <T>(url: string, params?: Record<string, any>): Promise<T> => service.get(url, { params }),
    post: <T>(url: string, data: any): Promise<T> => service.post(url, data),
    put: <T>(url: string, data: any): Promise<T> => service.put(url, data),
    delete: <T>(url: string): Promise<T> => service.delete(url),
    upload: (url: string, file: File): Promise<any> => {
      const formData = new FormData()
      formData.append('file', file)
      return service.post(url, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
    }
  }

export default http
  