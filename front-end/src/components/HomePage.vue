<template>
<header class="flex justify-center items-center fixed w-full top-0 z-50 drop-shadow-md">
  <h1 class="font-serif font-bold text-2xl text-white">Wrapped</h1>
</header>
<main>
  <div class = "w-full alt-93 bottom-0 fixed bg-gradient-to-b from-gray-100 overflow-y-auto snap-y snap-mandatory">
    <div v-for="country in wrapped"> <div v-for="trend, key in country"> <div v-for="news, key in trend">
          <div class="snap-center flex flex-col">
            <ul v-for="ne, key in news" class="flex flex-col alt-93 bottom-0 justify-end smh:justify-center sm:justify-center sm:y-14 sm:pt-7">
              <div class="tip bottom px-2 pb-1 drop-shadow-md z-20"><h2 class="font-serif tracking-wide text-gray-700 text-xl">{{key}}</h2></div>
              <div class="flex overflow-x-auto gap-6 snap-x snap-mandatory sm:snap-normal before:shrink-0 before:w-[20%] sm:before:w-[0%] after:shrink-0 after:w-[20%] sm:after:w-[0%] sm:horizontal sm:pb-14 pb-5">
                <li v-for="n in ne" class="basis-4/5 sm:basis-3/12 xl:basis-2/12 shrink-0 snap-center sm:snap-align-none">
                  <CardViewer image="./../assets/img_news.png" :title='n.title' :summary='n.summary' :popularity='n.popularity' :source='n.source'/>
                </li>
              </div>
            </ul>
          </div>
        </div>
    </div> </div> </div>
    <div class="fixed bottom-0 w-full transition-all duration-300 ease-in-out delay-150 -z-10"><svg id="wave" style="transform:rotate(0deg); transition: 0.3s" viewBox="0 0 1440 490" version="1.1" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="sw-gradient-0" x1="0" x2="0" y1="1" y2="0"><stop stop-color="rgba(62, 243, 197.009, 0.03)" offset="0%"></stop><stop stop-color="rgba(11, 255, 77.27, 0.56)" offset="100%"></stop></linearGradient></defs><path style="transform:translate(0, 0px); opacity:1" fill="url(#sw-gradient-0)" d="M0,294L60,253.2C120,212,240,131,360,130.7C480,131,600,212,720,253.2C840,294,960,294,1080,302.2C1200,310,1320,327,1440,351.2C1560,376,1680,408,1800,424.7C1920,441,2040,441,2160,375.7C2280,310,2400,180,2520,155.2C2640,131,2760,212,2880,236.8C3000,261,3120,229,3240,245C3360,261,3480,327,3600,351.2C3720,376,3840,359,3960,294C4080,229,4200,114,4320,114.3C4440,114,4560,229,4680,236.8C4800,245,4920,147,5040,98C5160,49,5280,49,5400,57.2C5520,65,5640,82,5760,106.2C5880,131,6000,163,6120,212.3C6240,261,6360,327,6480,367.5C6600,408,6720,425,6840,408.3C6960,392,7080,343,7200,285.8C7320,229,7440,163,7560,147C7680,131,7800,163,7920,212.3C8040,261,8160,327,8280,302.2C8400,278,8520,163,8580,106.2L8640,49L8640,490L8580,490C8520,490,8400,490,8280,490C8160,490,8040,490,7920,490C7800,490,7680,490,7560,490C7440,490,7320,490,7200,490C7080,490,6960,490,6840,490C6720,490,6600,490,6480,490C6360,490,6240,490,6120,490C6000,490,5880,490,5760,490C5640,490,5520,490,5400,490C5280,490,5160,490,5040,490C4920,490,4800,490,4680,490C4560,490,4440,490,4320,490C4200,490,4080,490,3960,490C3840,490,3720,490,3600,490C3480,490,3360,490,3240,490C3120,490,3000,490,2880,490C2760,490,2640,490,2520,490C2400,490,2280,490,2160,490C2040,490,1920,490,1800,490C1680,490,1560,490,1440,490C1320,490,1200,490,1080,490C960,490,840,490,720,490C600,490,480,490,360,490C240,490,120,490,60,490L0,490Z"></path><defs><linearGradient id="sw-gradient-1" x1="0" x2="0" y1="1" y2="0"><stop stop-color="rgba(62, 243, 166.348, 0.38)" offset="0%"></stop><stop stop-color="rgba(11, 255, 110.336, 1)" offset="100%"></stop></linearGradient></defs><path style="transform:translate(0, 50px); opacity:0.9" fill="url(#sw-gradient-1)" d="M0,294L60,285.8C120,278,240,261,360,261.3C480,261,600,278,720,253.2C840,229,960,163,1080,163.3C1200,163,1320,229,1440,245C1560,261,1680,229,1800,187.8C1920,147,2040,98,2160,106.2C2280,114,2400,180,2520,204.2C2640,229,2760,212,2880,236.8C3000,261,3120,327,3240,359.3C3360,392,3480,392,3600,334.8C3720,278,3840,163,3960,98C4080,33,4200,16,4320,49C4440,82,4560,163,4680,171.5C4800,180,4920,114,5040,81.7C5160,49,5280,49,5400,65.3C5520,82,5640,114,5760,130.7C5880,147,6000,147,6120,179.7C6240,212,6360,278,6480,326.7C6600,376,6720,408,6840,367.5C6960,327,7080,212,7200,147C7320,82,7440,65,7560,57.2C7680,49,7800,49,7920,98C8040,147,8160,245,8280,236.8C8400,229,8520,114,8580,57.2L8640,0L8640,490L8580,490C8520,490,8400,490,8280,490C8160,490,8040,490,7920,490C7800,490,7680,490,7560,490C7440,490,7320,490,7200,490C7080,490,6960,490,6840,490C6720,490,6600,490,6480,490C6360,490,6240,490,6120,490C6000,490,5880,490,5760,490C5640,490,5520,490,5400,490C5280,490,5160,490,5040,490C4920,490,4800,490,4680,490C4560,490,4440,490,4320,490C4200,490,4080,490,3960,490C3840,490,3720,490,3600,490C3480,490,3360,490,3240,490C3120,490,3000,490,2880,490C2760,490,2640,490,2520,490C2400,490,2280,490,2160,490C2040,490,1920,490,1800,490C1680,490,1560,490,1440,490C1320,490,1200,490,1080,490C960,490,840,490,720,490C600,490,480,490,360,490C240,490,120,490,60,490L0,490Z"></path><defs><linearGradient id="sw-gradient-2" x1="0" x2="0" y1="1" y2="0"><stop stop-color="rgba(62, 184.745, 243, 0.2)" offset="0%"></stop><stop stop-color="rgba(11, 234.334, 255, 0.15)" offset="100%"></stop></linearGradient></defs><path style="transform:translate(0, 100px); opacity:0.8" fill="url(#sw-gradient-2)" d="M0,294L60,310.3C120,327,240,359,360,351.2C480,343,600,294,720,302.2C840,310,960,376,1080,400.2C1200,425,1320,408,1440,351.2C1560,294,1680,196,1800,163.3C1920,131,2040,163,2160,220.5C2280,278,2400,359,2520,367.5C2640,376,2760,310,2880,269.5C3000,229,3120,212,3240,212.3C3360,212,3480,229,3600,245C3720,261,3840,278,3960,269.5C4080,261,4200,229,4320,236.8C4440,245,4560,294,4680,302.2C4800,310,4920,278,5040,228.7C5160,180,5280,114,5400,122.5C5520,131,5640,212,5760,269.5C5880,327,6000,359,6120,343C6240,327,6360,261,6480,212.3C6600,163,6720,131,6840,122.5C6960,114,7080,131,7200,130.7C7320,131,7440,114,7560,163.3C7680,212,7800,327,7920,359.3C8040,392,8160,343,8280,343C8400,343,8520,392,8580,416.5L8640,441L8640,490L8580,490C8520,490,8400,490,8280,490C8160,490,8040,490,7920,490C7800,490,7680,490,7560,490C7440,490,7320,490,7200,490C7080,490,6960,490,6840,490C6720,490,6600,490,6480,490C6360,490,6240,490,6120,490C6000,490,5880,490,5760,490C5640,490,5520,490,5400,490C5280,490,5160,490,5040,490C4920,490,4800,490,4680,490C4560,490,4440,490,4320,490C4200,490,4080,490,3960,490C3840,490,3720,490,3600,490C3480,490,3360,490,3240,490C3120,490,3000,490,2880,490C2760,490,2640,490,2520,490C2400,490,2280,490,2160,490C2040,490,1920,490,1800,490C1680,490,1560,490,1440,490C1320,490,1200,490,1080,490C960,490,840,490,720,490C600,490,480,490,360,490C240,490,120,490,60,490L0,490Z"></path></svg></div>
</main>
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

@media (min-height: 740px) {
    .smh\:justify-center {
        justify-content: center;
    }
}

@media (min-width: 640px) {
    .sm\:horizontal::before,
    .sm\:horizontal::after {
        content: '';
        flex: 1;
    }
}

header {
  background-color: #86EFAC;
  box-shadow: 0 1em 0.5em -0.5em rgba(126, 184, 124, 0.300);
  height: 7vh;
}

.alt-93 {
  height: 93vh;
}

.tip {
        position: relative;
        background-color: #BBF7D0;
        margin: 0px auto;
        color: transparent;
        text-align: center;
        border-radius: 10px;
}

.tip:after {
        content: "";
        position: absolute;
        width: 0;
        height: 0;
        border: 8px solid;
      }

.bottom:after {
        border-top-color: #BBF7D0;
        top: 100%;
        position: absolute;
        margin: 0px -8px;
}

</style>