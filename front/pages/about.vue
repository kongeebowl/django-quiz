<template>
  <div>
    <GoonerThing /><QuizCard
      v-for="question in data"
      :key="question.id"
      :question="question.question_text"
    />
  </div>
</template>

<script setup lang="ts">
const { data } = await useFetch("http://127.0.0.1:8000//api/questions");
console.log(data.value);
</script>
