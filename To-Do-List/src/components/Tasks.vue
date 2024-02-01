<template>
    <div  :key="task.id" v-for="task in tasks">
        <Task @get-categories="$emit('get-categories', task.categories)" @toggle-completed="$emit('toggle-completed', task.id)"  @toggle-reminder="$emit('toggle-reminder', task.id)" @delete-task="$emit('delete-task',task.id)" :task="task" />
    </div>
</template>

<script>
import Task from "./Task.vue"

    export default{
        name: 'Tasks',
        props:{
            tasks: Array,
            completed: Boolean
        },
        components:{
            Task,
        },
        emits:['delete-task', 'toggle-reminder']
    }
</script> 