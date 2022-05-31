<template>
<div class="text-gray-900 font-sans">
    <div class="flex-1 flex-wrap">
        <div class="w-full h-4/6 text-left">
            <a href="" class="c-card block bg-white rounded-2xl transform transition-all hover:-translate-y-2 duration-300 shadow-lg hover:shadow-2xl overflow-hidden">
                <div class="relative pb-44 overflow-hidden m-2">
                <img class="absolute inset-0 h-full w-full object-cover bg-green-300 border-white rounded-2xl " src="./../assets/img_news.png" alt="">
                </div>
                <div class="px-4 py-1 h-56 sm:h-52">
                <h2 class="mt-1 mb-1 font-bold"> {{title}} </h2>
                <p class="text-sm truncador">{{summary}}</p>
                </div>
                <div class="px-4 py-3 border-t border-b text-sm text-gray-700">
                <span class="mb-1">
                    <i class="mr-1 text-gray-900"></i> Popularity: {{popularity}}
                </span>      
                </div>
                <div class="px-4 py-3 text-xs text-gray-600"><span class="ml-1"> Source: {{source}} </span></div>
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

<style>

.truncador {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 6;
  -webkit-margin-collapse:discard;
}

</style>