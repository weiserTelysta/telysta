<template>
  <BaseHeadNavigationSimple></BaseHeadNavigationSimple>
  <div class="mainbody">
    <div class="login-container">
      <div class="glass-form">
        <h1 class="form-title">欢迎登录</h1>

        <form @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="email">邮箱</label>
            <input id="email" v-model="form.email" type="email" required placeholder="请输入注册邮箱">
          </div>

          <div class="form-group">
            <label for="password">密码</label>
            <input id="password" v-model="form.password" type="password" required placeholder="请输入密码" minlength="6" autocomplete="current-password">
          </div>

          <button type="submit" class="submit-btn">
            <span v-if="!loading">立即登录</span>
            <div v-else class="loader"></div>
          </button>

          <div class="form-footer">
            <router-link to="/register">注册账号</router-link>
            <router-link to="/forgot-password">忘记密码？</router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import authHttp from '@/api/authHttp'
import { errorMessages } from 'vue/compiler-sfc'
import BaseHeadNavigationSimple from '@/components/base-components/BaseHeadNavigationSimple.vue'

const router = useRouter()
const loading = ref(false)

const form = reactive({
  email: '',
  password: '',
})

const handleSubmit = async () => {
  try {
    loading.value = true

    const response = await authHttp.login(form.email, form.password);
    localStorage.setItem('token', response.access_token);
    console.log('登录成功', response);
    router.push({ name: 'home' });

  } catch (error) {
    console.error('登录失败:', error);
  } finally {
    loading.value = false;
  }
}
</script>

<style lang="scss" scoped>
@use 'sass:color';
@import "@/assets/css/color-system";


.mainbody {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background:
    linear-gradient(rgba(0 0 0 / 0.5), rgba(0 0 0 / 0.5)),
    url('@/assets/images/telystaimages/backgroundImage/bgsense-02.webp');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

.glass-form {
  background: rgba(255 255 255 / 0.1);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  padding: 2.5rem;
  width: 400px;
  box-shadow: 0 8px 32px rgba(0 0 0 / 0.1);
  border: 1px solid rgba(255 255 255 / 0.1);

  .form-title {
    color: $text-colors-light;
    text-align: center;
    margin-bottom: 2rem;
    font-size: 1.8rem;
    text-shadow: 0 2px 4px rgba(0 0 0 / 0.1);
  }

  .form-group {
    margin-bottom: 1.5rem;

    label {
      display: block;
      color: $text-colors-light;
      margin-bottom: 0.5rem;
      font-size: 0.9rem;
    }

    input {
      width: 100%;
      padding: 0.8rem;
      border: 1px solid rgba(255 255 255 / 0.2);
      border-radius: 8px;
      background: rgba(255 255 255 / 0.1);
      color: $text-colors-light;
      transition: all 0.3s;

      &:focus {
        outline: none;
        border-color: $color-primary;
        box-shadow: 0 0 0 3px rgba($color-primary, 0.2);
      }

      &::placeholder {
        color: rgba(255 255 255 / 0.6);
      }
    }
  }

  .submit-btn {
    width: 100%;
    padding: 1rem;
    background: $color-primary;
    margin-top: 10px;
    color: $text-colors-light;;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: 500;

    &:hover {
            background: color.adjust($color-primary, $lightness: -10%);
            }

    .loader {
      width: 24px;
      height: 24px;
      margin: 0 auto;
      border: 3px solid rgba(255 255 255 / 0.2);
      border-top-color: white;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }
  }

  .form-footer {
    margin-top: 1.5rem;
    display: flex;
    justify-content: space-between;

    a {
      color: rgba(255 255 255 / 0.8);
      font-size: 0.9rem;
      text-decoration: none;
      transition: color 0.3s;

      &:hover {
        color: white;
        text-decoration: underline;
      }
    }
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>