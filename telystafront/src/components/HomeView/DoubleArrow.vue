<template>
    <transition :name="isOpen ? 'rotate-up' : 'rotate-down'" mode="out-in">
        <div class="container-arrow" @click="handleClick">
            <div class="ripple-effect" v-if="showRipple"></div>
            <svg v-show="isOpen" t="1739019223177" class="icon" viewBox="0 0 1140 1024" version="1.1"
                xmlns="http://www.w3.org/2000/svg" p-id="6657" width="256" height="256">
                <path
                    d="M1080.905453 28.081184c0-7.878308-3.290694-15.708224-9.717225-21.254011-11.730356-10.133401-29.45171-8.836481-39.585112 2.893875L542.015621 576.610814 52.437804 9.730727c-10.133401-11.730356-27.854756-13.027276-39.585112-2.893875-11.730356 10.133401-13.027276 27.854756-2.893874 39.585111l510.822149 591.473185c5.33286 6.17489 13.085347 9.717225 21.244332 9.717225s15.911473-3.552014 21.244333-9.717225l510.822149-591.473185A28.021226 28.021226 0 0 0 1080.905453 28.081184z"
                    p-id="6658"></path>
                <path
                    d="M1080.905453 404.47849c0-7.878308-3.290694-15.708224-9.717225-21.254011-11.730356-10.133401-29.45171-8.836481-39.585112 2.893875L542.015621 952.998441 52.437804 386.118354c-10.133401-11.730356-27.854756-13.027276-39.585112-2.893875-11.730356 10.133401-13.027276 27.854756-2.893874 39.585111l510.822149 591.473185c5.33286 6.17489 13.085347 9.717225 21.244332 9.717225s15.911473-3.552014 21.244333-9.717225l510.822149-591.473185a27.99703 27.99703 0 0 0 6.813672-18.3311z"
                    p-id="6659"></path>
            </svg>
            <svg v-show="!isOpen" t="1739019195411" class="icon" viewBox="0 0 1140 1024" version="1.1"
                xmlns="http://www.w3.org/2000/svg" p-id="6427" width="256" height="256">
                <path
                    d="M3.132004 995.918816c0 7.878308 3.290694 15.708224 9.717226 21.254011 11.730356 10.133401 29.45171 8.836481 39.585111-2.893875L542.012158 447.398865l489.577817 566.880087c10.133401 11.730356 27.854756 13.027276 39.585111 2.893875 11.730356-10.133401 13.027276-27.854756 2.893875-39.585112L563.266169 386.104852c-5.33286-6.17489-13.085347-9.717225-21.244332-9.717225s-15.911473 3.552014-21.244333 9.717225L9.955355 977.587715a27.95638 27.95638 0 0 0-6.823351 18.331101z"
                    p-id="6428"></path>
                <path
                    d="M3.132004 619.52151c0 7.878308 3.290694 15.708224 9.717226 21.254011 11.730356 10.133401 29.45171 8.836481 39.585111-2.893875L542.021837 71.001559l489.577817 566.880087c10.133401 11.730356 27.854756 13.027276 39.585111 2.893875 11.730356-10.133401 13.027276-27.854756 2.893875-39.585111L563.266169 9.717225c-5.33286-6.17489-13.085347-9.717225-21.244332-9.717225s-15.911473 3.552014-21.244333 9.717225L9.955355 601.19041a27.974769 27.974769 0 0 0-6.823351 18.3311z"
                    p-id="6429"></path>
            </svg>

        </div>
    </transition>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const isOpenProps = withDefaults(
    defineProps<{
        isOpen: boolean;
    }>(),
    {
        isOpen: false,
    }
);


const showRipple = ref(false)

const handleClick = () => {
    showRipple.value = true
    setTimeout(() => showRipple.value = false, 600)
}
</script>

<style lang="scss" scoped>
.container-arrow {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 60px;

    // 点击动画效果实现
    transition: all 0.3s ease;
    padding: 8px;



    .icon {
        fill: #FB5349;
        width: 60px;
        height: 40px;
        transform: scaleX(1.5);
        cursor: pointer;
        animation: blink 5s infinite;

        &:active {
            transform: scale(1);
            transition-duration: 0.1s;
        }

        @keyframes blink {
            0% {
                opacity: 1;
            }

            50% {
                opacity: 0.5;
            }

            100% {
                opacity: 1;
            }
        }
    }
}

/* 专业级贝塞尔曲线 */
.rotate-up-enter-active,
.rotate-up-leave-active,
.rotate-down-enter-active,
.rotate-down-leave-active {
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.rotate-up-enter-from {
    opacity: 0;
    transform: rotate(-180deg) scaleX(1.5);
}

.rotate-up-leave-to {
    opacity: 0;
    transform: rotate(90deg) scaleX(1.5);
}

.rotate-down-enter-from {
    opacity: 0;
    transform: rotate(180deg) scaleX(1.5);
}

.rotate-down-leave-to {
    opacity: 0;
    transform: rotate(-90deg) scaleX(1.5);
}

//涟漪效果
.ripple-effect {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: radial-gradient(circle at center,
            rgba(251, 83, 73, 0.3) 0%,
            transparent 70%);
    animation: ripple 0.6s ease-out;
}

@keyframes ripple {
    from {
        transform: scale(0);
        opacity: 1;
    }

    to {
        transform: scale(2);
        opacity: 0;
    }
}
</style>