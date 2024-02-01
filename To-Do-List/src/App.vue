<template>
  <div class="nav-bar">
    <nav>
      <h1>To Do List</h1>
    </nav>
  </div>
  <div class="container">
    <Header @toggle-add-task="toggleAddTask" 
    title="Tasks" 
    :showAddTask="showAddTask"
    @go-home="goHome"
    /> 
    <div>
      <AddTask v-show="showAddTask" @add-task="addTask" />
    </div>
    <Tasks @get-categories="getCategories" @toggle-completed="toggleReminder" @toggle-reminder="toggleReminder"  @delete-task="deleteTask" :tasks="tasks"/>
  </div>
</template>

<script>
import Header from "./components/Header.vue"
import Tasks from "./components/Tasks.vue"
import AddTask from "./components/AddTask.vue"

export default{
  name: 'App',
  components:{
    Header,
    Tasks,
    AddTask
  },
  data(){
    return{
      tasks:[],
      showAddTask: false,
    }
  },
  methods:{

    toggleAddTask(){
      this.showAddTask = !this.showAddTask
      if (this.showAddTask){
        this.tasks = []
      }else{
        return this.goHome()
      }
    },

    getCategories(categories){
      this.tasks = this.tasks.filter((task) => task.categories == categories)
    },

    async goHome(){
      this.tasks = await this.fetchTasks()
      this.showAddTask = false
    },


    async deleteTask(id){
      const res = await fetch(`http://localhost:5000/tasks/${id}`, {
        method: 'DELETE'
      })
      res.status === 200 ? 
      (this.tasks = this.tasks.filter((task) => task.id !== id)) 
      : alert("Error deleting")
    },

    async toggleReminder(id){
      
      const taskToToggle = await this.fetchTask(id)
      const updTask = {...taskToToggle, reminder:!taskToToggle.reminder, completed:!taskToToggle.completed}

      const res = await fetch(`http://localhost:5000/tasks/${id}`, {
        method:'PUT',
        headers:{
          'Content-type':'application/json'
        },
        body: JSON.stringify(updTask)
      })

      const data = res.json()

      this.tasks = this.tasks.map((task) => task.id === id ? {
        ...task, reminder: data.reminder
      }: task
      )
      console.log(id)
    },
    async addTask(task){
      const res = await fetch('http://localhost:5000/tasks', {
        method:'POST',
        headers: {
          'Content-type':'application/json',
        },
        body:JSON.stringify(task)
      })

      const data = await res.json()

      this.tasks = [...this.tasks, data]

    },
    async fetchTasks(){
      const res = await fetch("http://localhost:5000/tasks")
      const data = await res.json()
      return data
    },
    async fetchTask(id){
      const res = await fetch(`http://localhost:5000/tasks/${id}`)
      const data = await res.json()
      return data
    }

  },
  async created(){
    this.tasks = await this.fetchTasks()
  },
}

</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: 'Poppins', sans-serif;
}

.nav-bar{
  text-align: center;
  padding: 1em 0;
  width: 100%;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.2);
  
}

.container {
  max-width: 600px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
  color: #000;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}

.btn:focus {
  outline: none;
}

.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}

</style>
