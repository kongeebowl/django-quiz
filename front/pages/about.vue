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
//use useFetch try ad figure it out because i get errors for some reason AUOWEGHAUIWEHAUIOWehUIOAWEHIOUEHAIOWUEHOIUAWEHOUI BHLFKBLKJSB
const { data } = await useFetch("/api/questions", {
  transform: (response) => response.data,
});
</script>
