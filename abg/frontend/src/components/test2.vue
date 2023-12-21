<template>
  <div fixed>
    <!-- <v-app-bar color="#5d54a4"> -->
    <v-img src="../../assets/Images/bottom.jpg">
      <v-layout wrap justify-center fill-height>
        <v-flex lg11 align-self-center>
          <v-card color="transparent" elevation="0">
            <v-layout wrap>
              <v-flex xs12 md2 text-center>
                <v-layout wrap justify-center>
                  <v-flex xs3 sm2 md6 align-self-center>
                    <v-img
                      text
                      src="../../assets/Images/ASccendo logo.png"
                      style="cursor: pointer"
                      @click="$router.push('/')"
                    ></v-img>
                  </v-flex>
                </v-layout>
                <!-- <router-link to="/" style="text-decoration: none"
                > -->

                <!-- </router-link
              > -->
              </v-flex>
              <v-flex xs12 md10 align-self-center>
                <v-layout wrap px-4 px-md-0>
                  <v-flex xs12 md2 text-center align-self-center>
                    <span
                      style="cursor: pointer"
                      class="titlefont2 text1"
                      @click="$router.push('/CareersPage')"
                      >Careers</span
                    >
                  </v-flex>

                  <v-flex xs12 md2 text-center align-self-center>
                    <span
                      style="cursor: pointer"
                      class="titlefont2 text1"
                      @click="$router.push('/contact')"
                      >Contact us</span
                    >
                  </v-flex>

                  <v-flex xs12 md2 text-center align-self-center>
                    <span
                      style="cursor: pointer"
                      class="titlefont2 text1"
                      @click="$router.push('/OurWorksPage')"
                      >Our Work</span
                    >
                  </v-flex>

                  <v-flex xs12 md2 text-center align-self-center>
                    <span
                      style="cursor: pointer"
                      class="titlefont2 text1"
                      @click="$router.push('/ServicesPage')"
                      >Services</span
                    >
                  </v-flex>

                  <v-flex xs12 md2 text-center align-self-center>
                    <span
                      style="cursor: pointer"
                      class="titlefont2 text1"
                      @click="$router.push('/contact')"
                      >Contact us</span
                    >
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
            <v-layout wrap justify-center py-3>
              <v-flex xs12 md3 text-center>
                <a
                  style="text-decoration: none"
                  href="https://www.linkedin.com/in/asccendo-technologies"
                >
                  <v-icon class="pr-6 social-login__icon">mdi-linkedin</v-icon>
                </a>

                <a
                  style="text-decoration: none"
                  href="https://www.facebook.com/Asccendo?mibextid=ZbWKwL"
                >
                  <v-icon class="pr-6 social-login__icon">mdi-facebook</v-icon>
                </a>
              </v-flex>
            </v-layout>
            <v-layout wrap justify-center py-1>
              <v-flex xs12 text-center>
                <span class="titlefont2" style="font-color:white;">
                  © Copyrights all reserved
                </span>
              </v-flex>
            </v-layout>
            <v-layout wrap justify-center>
              <v-flex
                pb-2
                xs12
                text-center
                class="arvo"
                style="font-size: 15px"
              >
                <span> 2022-2023 </span>
              </v-flex>
            </v-layout>
          </v-card>
          <v-card xs9> </v-card>
        </v-flex>
      </v-layout>
    </v-img>
    <!-- </v-app-bar> -->
  </div>
</template>
<script>
export default {};
</script>
<style >
.router-link {
  text-decoration: none;
}
</style>