// src/store/userStore.ts
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
  // 登录状态
  const isLoggedIn = ref(false)
  
  // 用户信息
  const userInfo = ref({
    username: '',
    avatar: ''
  })

  // 登录方法
  const login = async (credentials: { username: string; password: string }) => {
    try {
      // 调用登录接口
      const res = await api.login(credentials)
      
      // 更新状态
      isLoggedIn.value = true
      userInfo.value.username = res.data.username
      
      // 持久化存储
      localStorage.setItem('token', res.data.token)
    } catch (error) {
      throw error
    }
  }

  // 自动初始化
  const initialize = () => {
    const token = localStorage.getItem('token')
    if (token) {
      isLoggedIn.value = true
      // 这里可以添加获取用户信息的逻辑
    }
  }

  return { isLoggedIn, userInfo, login, initialize }
})