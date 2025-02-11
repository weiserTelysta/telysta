<template>
    <div class="container-background" :class="{ 'full-screen': !isOpen, 'banner-size': isOpen }">
        <div class="latin-title cinzel-fonts">
            <div class="telysta miss-fajardose-regular">Telysta</div>
            <div class="sub line-1" v-show="!isOpen">Invicta Sub Rubro Dracone</div>
            <div class="sub line-2" v-show="!isOpen">Flammis Antiquis Et Sanguine Recenti</div>
            <div class="sub line-3" v-show="!isOpen">Coronam Gloriæ Per Maledicta Gerens</div>
            <div class="sub line-4" v-show="!isOpen">Flos Imperii Nunquam Defessus.</div>
        </div>
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
    }, 60000);
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
    position: relative;
    overflow: hidden;
    background-color: aliceblue;

    box-shadow: 0 1px 5px;
    transition: all 0.5s ease;


    #background-image {
        position: relative;
        height: 100%;
        width: 100%;
        object-fit: cover;

        transition: transform 15s ease;
    }

    /* 在hover时，放大图片 */
    #background-image:hover {
        transform: scale(1.05);
        transition: transform 15s ease;
    }


    .image-container {
        position: relative;
    }

    .container-doublearrow {
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 4;
    }
}

.full-screen {
    height: 100vh;
    width: 100%;

    .telysta {
        font-size: 220px;
        transition: transform 15s ease;
    }
}

.banner-size {
    position: relative;
    height: 500px;
    width: 100%;

    &::after {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.3);
        z-index: 1;
        pointer-events: none;
    }

    .telysta {
        font-size: 280px;
    }

}

.latin-title {
    width: auto;
    z-index: 3;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: grid;
    place-items: center;
    color: white;
    // pointer-events: none;



    .telysta {

        font-weight: 500;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 1);


    }

    .sub {
        font-size: 22px;
        font-weight: 400;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 1);
    }
}
</style>