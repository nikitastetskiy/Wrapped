<template>
<div class="text-gray-900 font-sans">
    <div class="flex-1 flex-wrap">
        <div class="w-full h-5/6 text-left">
            <a href="" class="c-card block bg-white shadow-md hover:shadow-xl rounded-lg overflow-hidden">
                <div class="relative pb-56 overflow-hidden">
                <img class="absolute inset-0 h-full w-full object-cover" src="./../assets/img_news.png" alt="">
                </div>
                <div class="p-4 h-36">
                <h2 class="mt-1 mb-1 font-bold"> {{title}} </h2>
                <p class="text-sm">{{summary}}</p>
                </div>
                <div class="p-4 border-t border-b text-sm text-gray-700">
                <span class="mb-1">
                    <i class="mr-1 text-gray-900"></i> Popularity: {{popularity}}
                </span>      
                </div>
                <div class="p-4 text-xs text-gray-600"><span class="ml-1"> Source: {{source}} </span></div>
            </a>
        </div> 
    </div>
</div>
</template>

<script>
export default {
  name: "CardViewer",
  props: {
    image: String,
    title: String,
    summary: String,
    popularity: String,
    source: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only 
<style scoped>
.c-card {
  img {    
    transition: transform .3s ease-in-out; 
  }
  
  &:hover {
    img {
      transform: scale(1.05)
    }
  }
}
</style>
-->