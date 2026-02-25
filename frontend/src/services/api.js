const baseHeaders = {
  'Content-Type': 'application/json'
}

export async function fetchTasks() {
  const response = await fetch('/api/tasks', { headers: baseHeaders })
  return response.json()
}

export async function createTask(title) {
  const response = await fetch('/api/tasks', {
    method: 'POST',
    headers: baseHeaders,
    body: JSON.stringify({ title })
  })
  return response.json()
}
