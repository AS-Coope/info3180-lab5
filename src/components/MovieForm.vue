<template>
    <form @submit.prevent="saveMovie" method="post" enctype="multipart/form-data" id="movieForm">
        <div class="form-group mb-3">
            <label for="title" class="form-label">
                Movie Title
            </label>
            <input type="text" name="title" class="form-control">
            <label for="description" class="form-label">
                Movie Description
            </label>
            <input type="textarea" name="description" class="form-control">
            <input type="file" class="form-control"/>
            <button type="submit" name="submit" class="btn btn-primary">Upload file</button>
        </div>
    </form>
</template>

<script setup>
//const props = defineProps(['movie'])
//const emit = defineEmits(['edit', 'remove'])
    import {ref, onMounted} from "vue";
    let csrf_token = ref("");
    onMounted(()=>{
        getCsrfToken();
    })
    function saveMovie() {

        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);
        fetch("/api/v1/movies", { 
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
        .then(response => { 
                return response.json(); 
        }) 
        .then(data => { 
            // display a success message 
            console.log(data); 
        }) 
        .catch(error => { 
            console.log(error); 
        })
    }
    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((reponse) => reponse.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
        .catch(error => { 
            console.log(error); 
        })
    }
</script>