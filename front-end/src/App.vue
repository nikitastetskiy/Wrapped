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

html {
  height: 100%;
  width: 100%;
}

body {
  height: 100%;
  width: 100%;
}

</style>
