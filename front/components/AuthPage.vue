<template>
    <section  class="bg-gray-50 dark:bg-gray-900">
  <div data-theme="coffee" class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
          <img class="w-8 h-8 mr-2" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" alt="awesome logo">
          Quizzes ami right    
      </a>
      <div class="w-full bg-primary-content rounded-lg md:mt-0 sm:max-w-md xl:p-0 ">
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 class="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl dark:text-white">
                  Sign in to
                   your account
              </h1>
              <form class="space-y-4 md:space-y-6" action="#" @submit.prevent="handleLogin()">
                  <div>
                      <label for="email" class="block mb-2 text-sm font-medium text-white">Your username</label>
                      <input name="username"  class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="emails amiright" v-model="username">
                  </div>
                  <div>
                      <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                      <input  name="password" id="password" placeholder="paswords am i right" class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"v-model="password">
                  </div>
                  <div class="flex items-center justify-between">
                      
                  </div>
                  <button type="submit" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Sign in</button>
                  
              </form>
          </div>
      </div>
  </div>
</section>
</template>

<script setup lang="ts">
const config =useRuntimeConfig()
const username = ref('')
const password = ref('')
const error = ref(null)

const handleLogin = async () => {
  try {
    
    const res = await fetch('http://localhost:8000/api/signin/', {
      method: 'POST',
      credentials: 'include', 
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    })
    console.log(username.value)

    console.log(res)
    const data = await res.json()
    console.log(data.value)

    if (!res.ok) {
        alert("no")
      error.value = data.error
      console.log(error.value)
    } else {
        alert("yes")
      error.value = null
      
    }
    console.log(error)
  } catch (err) {
    console.log(err)
  }
}
</script>

<style scoped>

</style>