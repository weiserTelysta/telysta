<template>
    <div class="firstcontainer">
        <nav class="secondcontainer">
            <div class="right">
                <h1 @click="goToHome">telysta</h1>
            </div>
            <div class="left">
                <HeadNavBtn class="login" @click="goToLogin">登录</HeadNavBtn>
            </div>
        </nav>
    </div>

</template>

<script lang="ts" setup>
import { ref } from 'vue';
import HeadNavBtn from './button/HeadNavBtn.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const goToLogin = () => {
    router.push({ name: 'login' });
};
const goToHome = () => {
    router.push({ name: 'home' });
}
</script>

<style lang="scss" scoped>
@use "sass:map";
@import "@/assets/css/color-system";

.firstcontainer {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: map.get($color-neutral, "0");

    nav {
        height: 60px;
        display: flex;
        justify-content: space-between;
        background-color: transparent;

        z-index: 10;


        h1 {
            font-family: Cinzel;
            font-size: 30px;
            font-weight: 600;
            color: $color-primary;
            cursor: pointer;
            transition: all .2s ease;

            &:hover {
                color: $color-primary-light;

            }
        }

        >div {
            display: flex;
            align-items: center;
            justify-content: center;
        }

    }

}
</style>