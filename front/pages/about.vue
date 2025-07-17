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
//use useFetch try ad figure it out because i get errors for some reason AUOWEGHAUIWEHAUIOWehUIOAWEHIOUEHAIOWUEHOIUAWEHOUI BHLFKBLKJSB

const { data } = await useFetch("http://127.0.0.1:8000//api/questions");
console.log(data.value);
</script>
