<template>
  <div class="container-window">
    <div class="container-navigation firstcontainer" v-show="backgroundIsopenStore.isOpen">
      <BaseHeadNavigation></BaseHeadNavigation>
    </div>
    <div class="container-back">
      <HomeBackground />
    </div>
    <div class="container-body" v-show="backgroundIsopenStore.isOpen">
      <div class="content-main firstcontainer">
        <HomeMainContent></HomeMainContent>
      </div>
      <BaseFoot></BaseFoot>
    </div>
  </div>

</template>

<script lang="ts" setup>
import HomeBackground from '@/components/HomeView/HomeBackground.vue';
import BaseFoot from '@/components/base-components/BaseFoot.vue';
import BaseHeadNavigation from '@/components/base-components/BaseHeadNavigation.vue';
import HomeMainContent from '@/components/HomeView/HomeMainContent.vue';  

import { useBackgroundIsopenStore } from '@/stores/useBackgroundIsopenStore';

const backgroundIsopenStore = useBackgroundIsopenStore();
</script>

<style lang="scss" scoped>
.container-window {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.container-navigation{
  display: flex;
  align-items: center;
  justify-content: center;
}

.container-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.content-main {
  flex: 1;

  // width: 100%;
  background-color: aliceblue;
}

HomeFoot {
  margin-top: auto; 
}
</style>