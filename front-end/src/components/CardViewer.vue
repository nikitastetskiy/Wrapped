<template>
<div class="text-gray-900 font-sans">
    <div class="flex-1 flex-wrap animation transform transition-all duration-300">
        <div class="num"> 1 </div>
        <div class="w-full h-4/6 text-left">
            <a href="" class="c-card block bg-white rounded-2xl border-amber-100 border-x border-b shadow-lg overflow-hidden animation-shadow transform transition-all duration-300">
                <div class="relative pb-44 overflow-hidden m-2">
                <img class="absolute inset-0 h-full w-full object-cover bg-amber-300 border-white rounded-2xl " src="./../assets/michael.jpg" alt="">
                </div>
                <div class="px-4 py-1 h-56 sm:h-52">
                <h2 class="mt-1 mb-1 font-bold"> {{title}} </h2>
                <p class="text-sm truncador">{{summary}}</p>
                </div>
                <div class="px-4 py-3 border-t border-b border-amber-100 text-sm text-gray-700">
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

@media (hover: hover) and (pointer: fine) {
  .animation-shadow:hover {
  --tw-shadow: 0 20px 25px -12px rgb(0 0 0 / 0.35);
    --tw-shadow-colored: 0 20px 25px -12px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }
}

@media (hover: hover) and (pointer: fine) {
  .animation:hover {
    --tw-translate-y: -0.5rem/* -8px */;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
  }
}

.truncador {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 8;
  -webkit-margin-collapse:discard;
}


.num {
  margin: 0px auto;
  background-color: white;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  color: black;
  vertical-align: top;
  text-align: center;
  transform: translateY(50%);
}

</style>