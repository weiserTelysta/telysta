<template>
    <div id ="navbtn">
        <slot></slot>
    </div>
</template>

<script lang="ts" setup>

</script>

<style lang="scss" scoped>
#navbtn{
    font-size: 14px;
    color: $color-primary;
    border-radius: 5px;
    padding:8px 18px;
    transition: all 0.5s ease;
    cursor: pointer;

    &:hover{
        background-color: $color-primary-alpha;
    }

    &.login{
        background-color: $color-primary;
        color: white;

        &:hover{
            background-color: $color-primary-light;
        }
    }
}
</style>