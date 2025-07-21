<template>
  <div>
    <h1 class="text-3xl font-bold font-serif text-green-100">
      {{ props.question }}
    </h1>
    <ul class="list-disc pl-5">
      <li
        
        class="text-lg text-gray-200"
      >
      </li>
      <button @click="">Submit</button>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";

const props = defineProps<{
  question: string;

}>();
</script>

<style scoped></style>
