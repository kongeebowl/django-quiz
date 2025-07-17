<template>
    <div>
     <AuthPage :users="data"/>
     
    </div>
</template>

<script setup lang="ts">
const data = ref<User[]|null>(null)
async function getUsers(){
    try {
    const response = await fetch("http://127.0.0.1:8000/api/users/");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const fetched = await response.json();
    data.value = fetched
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
  }
}
onMounted(async () => {
 await getUsers()
})
</script>

<style scoped>

</style>