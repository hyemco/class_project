<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand class="ms-4">My Tube</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item :to="{name: 'home'}">Home</b-nav-item>
        <b-nav-item :to="{name: 'search'}">Search</b-nav-item>
        <b-nav-item :to="{name: 'later'}">Later</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {

}
</script>

<style>

</style>