<template>
  <header class="flex justify-center items-center h-10 sm:h-14">
    <h1 class="font-serif text-2xl relative">Wrapped</h1>
  </header>
  <div>
    <div class = "w-scren h-screen bg-gradient-to-t from-gray-100 to-gray-300 dark:bg-slate-900 overflow-y-auto overflow-scroll snap-y snap-mandatory">
      <ul>
        <li v-for="country in wrapped">
          <li v-for="trend, key in country">
            <li v-for="news, key in trend">
              <div class="">
                <div class="snap-center relative flex-col w-screen h-screen">
                  <li v-for="ne, key in news" class="py-11">
                    <h2 class="inline-block px-2 py-1 leading-none shadow-xl rounded-lg overflow-hidden font-semibold font-serif tracking-wide text-2xl">{{key}}</h2>
                    <div class="flex sm:justify-center overflow-x-auto gap-6 snap-x snap-mandatory sm:snap-normal before:shrink-0 before:w-[20%] sm:before:w-[0%] after:shrink-0 after:w-[20%] sm:after:w-[0%] py-2">
                      <li v-for="n in ne" class="basis-4/5 sm:basis-3/12 shrink-0 snap-center sm:snap-align-none">
                        <CardViewer image="./../assets/img_news.png" :title='n.title' :summary='n.summary' :popularity='n.popularity' :source='n.source'/>
                      </li>
                    </div>
                  </li>
                </div>
              </div>
            </li>
          </li>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import CardViewer from "./CardViewer.vue";
export default {
  data() {
    const data = require("../../../db/database.json");
    return {
      wrapped: data,
    };
  },
  components: {
    CardViewer: CardViewer,
  },
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
header {
  background-color: #fff;
  box-shadow: 0 1em 0.5em -0.5em rgb(181, 181, 181);
}
</style>