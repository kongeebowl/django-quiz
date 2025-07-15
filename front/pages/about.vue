<template>
  <div><GoonerThing /></div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";

async function getData() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/questions/");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
  }
}

onMounted(async () => {
  await getData();
});
</script>
