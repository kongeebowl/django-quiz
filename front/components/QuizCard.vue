<template>
  <div>
    <h1 class="text-3xl font-bold font-serif text-green-100">
      {{ props.question }}
    </h1>
    <ul class="list-disc pl-5">
      <li
        v-for="(choice, index) in choices"
        :key="index"
        class="text-lg text-gray-200"
      >
        {{ choice }}
      </li>
      <button @click="">Submit</button>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";

const props = defineProps<{
  question: string;
  choices: string[];
}>();
</script>

<style scoped></style>
