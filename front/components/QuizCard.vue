<template>
  <div class="max-w-xl mx-auto p-6 bg-white rounded-lg shadow-md mt-10">
    <h2 class="text-2xl font-semibold mb-4">{{ question.question_text }}</h2>

    <input
      v-model="userAnswer"
      type="text"
      placeholder="Type your answer here"
      @keydown.enter.prevent="submitAnswer"
      class="w-full border border-gray-300 rounded-md px-4 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-400"
    />

    <button
      @click="submitAnswer"
      :disabled="loading"
      class="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition-colors disabled:opacity-50"
    >
      {{ loading ? "Submitting..." : "Submit" }}
    </button>

    <div v-if="result" class="mt-6">
      <p class="text-lg font-medium mb-2">
        {{ result.message }}
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  question: Question;
}>();

const API_BASE_URL = "http://127.0.0.1:8000/api";

const userAnswer = ref("");
const result = ref<CheckResponse | null>(null);
const loading = ref(false);

const submitAnswer = async () => {
  loading.value = true;
  result.value = null;

  try {
    const response = await fetch(
      `${API_BASE_URL}/check/${props.question.id}/`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_answer: userAnswer.value }),
      }
    );

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data: CheckResponse = await response.json();
    result.value = data;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};
</script>
