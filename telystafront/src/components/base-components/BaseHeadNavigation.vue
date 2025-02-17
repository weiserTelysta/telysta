<template>
    <nav class="secondcontainer">
        <div class="right">
            <h1>Telysta</h1>
        </div>
        <div class="left">
            <HeadNavBtn class="login" @click="goToLogin">登录</HeadNavBtn>
        </div>
    </nav>
    
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import HeadNavBtn from './button/HeadNavBtn.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const goToLogin = () => {
  router.push({ name: 'login' });
};
</script>

<style lang="scss" scoped>
nav {
    height: 60px;
    display: flex;
    justify-content: space-between;

    h1 {
        font-family: Cinzel;
        font-size: 30px;
        font-weight: 600;
        color: $color-primary;
        cursor: pointer;
        transition: all .5s esae;

        &:horver {
            color: $color-primary-light;
        }
    }

    >div {
        display: flex;
        align-items: center;
        justify-content: center;
    }
}
</style>