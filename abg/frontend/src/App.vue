<template>
    <v-app>
    <v-main>
      <v-layout fill-height  wrap style="background-color:#white">
        <v-flex xs12>
          <Header />
          

<router-view>
</router-view>
<Footer/>
        </v-flex>
      </v-layout>
     
    </v-main>
  </v-app>
</template>

<script>
import "./assets/style/fonts.css";
import "./assets/style/style.css";
import Header from './components/HeaderPage';
import Footer from './components/FooterPage';

export default {
  name: 'App',

  components: {
    Header,
    Footer,
  },

  data: () => ({
    //
  }),
};
</script>
