<template>
  <div>
    <GoonerThing /><QuizCard
      v-for="question in data"
      :key="question.id"
      :data="question"
    />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

const data = ref([]);

async function getData() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/quizzes/");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    data.value = await response.json();
    console.log(data);
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
  }
}

onMounted(async () => {
  await getData();
});
</script>
