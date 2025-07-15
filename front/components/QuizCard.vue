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
      <button @click="changeAnswered">Submit</button>
    </ul>
    <p v-if="answered" class="mt-4 text-lg text-gray-300">
      Answer: {{ props.answer }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { defineProps, ref } from "vue";

const answered = ref(false);

function changeAnswered() {
  answered;
}

const props = defineProps<{
  question: string;
  choices: string[];
  answer: string;
}>();
</script>

<style scoped></style>
