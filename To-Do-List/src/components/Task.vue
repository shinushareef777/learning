<template>
    <div @dblclick="$emit('toggle-reminder', task.id)" :class="[task.completed ? 'completed': 'reminder', 'task']">
        <small @click="$emit('get-categories', task.categories)">{{task.categories}}</small>
        <h3>{{task.text}}
            <div class="close-check">
                <input @input="$emit('toggle-completed', task.id)"  type="checkbox" v-model="task.completed">
                <i @click="$emit('delete-task', task.id)" class="fas fa-times"></i>
            </div> 
        </h3>
        <p>{{task.day}}</p>
    </div>
</template>

<script>

    export default{
        name: 'Task',
        props:{
            task: Object
        },
    }
</script>

<style scope>

    .fas{
        color: red;
    }
    .task{
        background: #f4f4f4;
        margin: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }

    .task.reminder{
        border-left: 5px solid green;
    }

    .task.completed{
        text-decoration: line-through;
        background-color: rgba(70, 130, 180, 0.2);
    }

    .close-check{
        display: flex;
        justify-content: space-around;
        width: 60px;
    }
    
    .close-check input, i{
        width: 20px;
        height: 20px;
    }

    small:hover{
        color: teal;
    }

    .task h3{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
</style>