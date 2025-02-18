<template>
    <BaseHeadNavigationSimple></BaseHeadNavigationSimple>
    <div class="mainbody">
        <div class="register-container">
            <div class="glass-form">
                <h1 class="form-title">注册账号</h1>

                <form @submit.prevent="handleSubmit">
                    <div class="form-group">
                        <label for="email">邮箱</label>
                        <input id="emial" v-model="form.email" type="email" required placeholder="请输入注册邮箱">
                        <transition name="fade">
                            <p v-if="emailError" class="error-msg">请输入有效的邮箱地址</p>
                        </transition>
                    </div>

                    <div class="form-group">
                        <label for="username">用户名</label>
                        <input type="text" id="username" v-model="form.username" required placeholder="请输入用户名">
                        <transition name="fade">
                            <p v-if="usernameError" class="error-msg">用户名长度不能少于3个字符</p>
                        </transition>
                    </div>

                    <div class="form-group">
                        <label for="password">密码</label>
                        <input id="password" v-model="form.password" required type="password" placeholder="请输入密码"
                            minlength="8" maxlength="20" autocomplete="current-password">
                        <transition name="fade">
                            <p v-if="passwordError" class="error-msg">密码长度需在6到20个字符之间</p>
                        </transition>
                    </div>

                    <div class="form-group">
                        <label for="password">确认密码</label>
                        <input id="password" v-model="form.confirmpassword" required type="password" placeholder="请输入密码"
                            minlength="8" maxlength="20" autocomplete="current-password">
                        <transition name="fade">
                            <p v-if="!passwordMatch" class="error-msg">两次输入的密码不一致</p>
                        </transition>
                    </div>

                    <button v-if="!emailsent" type="submit" class="submit-btn">
                        <span v-if="!loading">立即注册</span>
                        <div v-else class="loader"></div>
                    </button>
                    
                    <div class="form-footer">
                        <router-link to="/login">已有账号，登录</router-link>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import BaseHeadNavigationSimple from '@/components/base-components/BaseHeadNavigationSimple.vue'
import { reactive, ref } from 'vue';
import authHttp from '@/api/authHttp';
import { useRouter } from 'vue-router'
import { computed } from 'vue';
import { AxiosError } from 'axios';
import {watch} from 'vue';

const router = useRouter()
const loading = ref(false);
const emailsent = ref(false)

// 表单设置
const form = reactive({
    email: '',
    password: '',
    confirmpassword: '',
    username: '',
    telephone: '',

})

// 错误验证
// const emailError = ref(false)
// const usernameError = ref(false)
// const passwordError = ref(false)

// 错误验证
const emailError = computed(() => !/\S+@\S+\.\S+/.test(form.email))
const usernameError = computed(()=> (form.username.length < 3 && form.username.length > 20))
const passwordError = computed(()=>form.password.length < 8 && form.password.length > 20)
const passwordMatch = computed(() => form.password === form.confirmpassword)



const formValid = computed(() =>
    form.email &&
    form.username.length < 60 &&
    form.password.length >= 8 &&
    form.password.length < 20 &&
    passwordMatch.value
)
// 错误接口
interface ErrorResponse {
    email?: string[];  // 后端可能返回的邮箱错误字段
}
// 定义 AxiosError 类型
interface CustomAxiosError extends AxiosError<ErrorResponse> { }

// 类型守卫：检查 error 是否是 AxiosError 类型
function isAxiosError(error: unknown): error is CustomAxiosError {
    return (error as CustomAxiosError).isAxiosError === true;
}


// 注册按钮
const handleSubmit = async () => {
    if (!formValid.value) return

    try {
        loading.value = true;

        const response = await authHttp.register(form.email, form.username, form.password);
        console.log('注册成功', response)
        emailsent.value = true;
        // router.push({ name: 'login', query: { registered: 'true' } })
    } catch (error) {
        if (isAxiosError(error)) {
            // 确保 error 是 Axios 错误类型
            if (error.response) {
                // 检查 response 是否存在并且数据是否包含 email 字段
                if (error.response.data.email) {
                    alert(`该邮箱已经被注册：${error.response.data.email[0]}`);
                } else {
                    alert(`注册失败：${error.response.statusText}`);
                }
            } else {
                alert('无法连接到服务器，请检查网络连接');
            }
        } else {
            // 处理非 Axios 错误
            console.error('非预期错误类型:', error);
            alert('系统发生意外错误');
        }
    } finally {
        loading.value = false;
    }
}

// 监听邮箱，发生更改就立刻重启注册按钮

watch(form, (newValue, oldValue) => {
    emailsent.value = false;
});
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
            border: 1px solid rgba(255 255 255 / 0.1);
            border-radius: 8px;
            background-color: rgba(255 255 255 / 0.1);
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
        background-color: $color-primary;
        margin-top: 10px;
        color: $text-colors-light;
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

@keyframes shake {
    0% {
        transform: translateX(0);
    }

    25% {
        transform: translateX(-4px);
    }

    50% {
        transform: translateX(4px);
    }

    75% {
        transform: translateX(-4px);
    }

    100% {
        transform: translateX(0);
    }
}
</style>