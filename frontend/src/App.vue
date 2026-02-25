<template>
  <div class="shell">
    <header>
      <h1>Awesome App</h1>
      <p>Vue + FastAPI (Django-style backend layout)</p>
    </header>
    <main>
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.shell {
  max-width: 760px;
  margin: 0 auto;
  padding: 2rem 1rem;
  font-family: Inter, system-ui, -apple-system, sans-serif;
}
header h1 {
  margin-bottom: 0.4rem;
}
header p {
  color: #4b5563;
}
</style>
