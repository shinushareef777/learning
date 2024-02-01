<template>
    <header>
        <h2 @click="$emit('go-home')">{{title}}</h2>
        <Button @btn-click="$emit('toggle-add-task')" 
        :text="showAddTask ? 'Close': 'Add Task' "  
        :color="showAddTask ? '#BD2629': '#29A065' "/>
    </header>
    
</template>

<script>
import Button from './Button.vue'

    export default{
        name: 'Header',
        props:{
            title: String,
            showAddTask: Boolean

        },
        components:{
            Button
        }
    }
</script>

<style scoped>
    header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    header h2{
        cursor: pointer;
    }

    header h2:hover{
        color: steelblue;
    }
</style>



