import { defineStore } from 'pinia';

const useBackgroundIsopenStore = defineStore('isOpen',{
    state:()=>({
        isOpen :false,
    }),
    actions:{
        toggleIsopen(){
            this.isOpen = !this.isOpen;
        }
    }
});

export {useBackgroundIsopenStore};