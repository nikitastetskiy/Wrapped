<template>
  <HomePage />
</template>

<script>
import HomePage from "./components/HomePage.vue";

export default {
  name: "App",
  components: {
    HomePage,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

*{
  margin:0;
  padding:0;
}

body{
  background: #EEEEE3;
  min-height: 100vh;
  min-height: fill-available;
  min-height: -moz-available;
  min-height: -webkit-fill-available;
}

html {
  height: fill-available;
  height: -webkit-fill-available;
  scroll-behavior: smooth;
}
</style>
