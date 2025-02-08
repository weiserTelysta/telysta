<template>
    <div class="container-background" :class="{ 'full-screen': !isOpen, 'banner-size': isOpen }">
        <img :key="Index" :src="images[Index]" alt="Telysta(；´ﾟωﾟ｀人)图片损坏啦" id="background-image" draggable="false">
        <div class="container-doublearrow">
            <DoubleArrow :isOpen="isOpen" @click="toggleArrow"></DoubleArrow>
        </div>
    </div>


</template>

<script lang="ts" setup>
import { ref, computed, onMounted } from "vue";
import DoubleArrow from "./DoubleArrow.vue";

import telysta_day_01 from '@/assets/images/telystaimages/telysta_day_01.png';
import telysta_day_02 from '@/assets/images/telystaimages/telysta_day_02.png';
import telysta_day_03 from '@/assets/images/telystaimages/telysta_day_03.png';
import telysta_day_04 from '@/assets/images/telystaimages/telysta_day_04.png';
import telysta_day_05 from '@/assets/images/telystaimages/telysta_day_05.png';
import telysta_day_06 from '@/assets/images/telystaimages/telysta_day_06.png';

let preloadedimage: HTMLImageElement | null = null;

let isOpen = ref(false);


const images = ref<string[]>([
    telysta_day_05,
    telysta_day_01,
    telysta_day_04,
    telysta_day_06,
    telysta_day_02,
    telysta_day_03
]);

const Index = ref<number>(0);

const preLoadedNextImage = () => {
    const nextIndex = (Index.value + 1) % images.value.length;
    const preloadedimage = new Image();
    preloadedimage.src = images.value[nextIndex];
}

onMounted(() => {
    preLoadedNextImage();
    setInterval(() => {
        nextImage();
    }, 10000);
});

// 切换到下一张图片
function nextImage() {
    Index.value = (Index.value + 1) % images.value.length;
    preLoadedNextImage();
}

// 切换到上一张图片
function prevImage() {
    Index.value = (Index.value - 1 + images.value.length) % images.value.length;
    preLoadedNextImage();
}

// 组件切换
function toggleArrow() {
    isOpen.value = !isOpen.value;
}
</script>

<style lang="scss" scoped>
.container-background {
    overflow: hidden;
    position: relative;
    top: 0;
    // height: 100vh;
    // width: 100%;
    background-color: aliceblue;


    #background-image {
        position: absolute;
        height: 100%;
        width: 100%;
        object-fit: cover;
        transition: opacity 0.1s ease, transform 10s ease;
    }

    #background-image:hover {
        transform: scale(1.05);
        transition: transform 10s ease;
    }


}

.full-screen {
    height: 100vh;
    width: 100%;
}

.banner-size {
    height: 600px;
    /* 根据需要调整 */
    width: 100%;
}

.container-doublearrow {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
}
</style>