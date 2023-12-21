<template>
  <div class="app" style="background-color: #f7f7f7">
    <!-- <v-app-bar color="#5d54a4"> -->
    <v-layout
      wrap
      justify-center
      class="hidden-sm-and-down gradtop"
      style="height: 95px"
    >
      <v-flex xs12 class="fixItem">
        <!-- <v-img src="../../assets/Images/hd.jpg"> -->
        <v-layout wrap justify-center fill-height>
          <v-flex xs12 align-self-center>
            <v-card color="transparent" elevation="0">
              <v-layout wrap>
                <v-flex md3 xl3 pa-2>
                  <v-layout wrap justify-center>
                    <v-flex @click="$router.push('/')" xs8 xl5 align-self-center>
                      <v-img
                        style="cursor: pointer"
                        text
                        src="../assets/Images/logoorg.png"
                        height="80px"
                      ></v-img>
                    </v-flex>
                  </v-layout>
                  <!-- </router-link
                > -->
                </v-flex>
                <v-layout wrap justify-end>
                  <!-- <v-flex xs1 pt-1><a class="interSB" style="text-decoration:none; color:white" href="/#about">About</a></v-flex> -->
                  <v-flex align-self-center xs8>
                    <v-layout wrap justify-center>
                      <v-flex
                        xs2
                        class="interSB"
                        style="text-align: justify"
                        text-left
                        v-for="(item, i) in category"
                        :key="i"
                      >
                        <router-link
                          :to="item.route"
                          :href="item.path"
                          style="text-decoration: none"
                        >
                          <span
                            style="
                              cursor: pointer;
                              text-decoration: none;
                              color: black;
                            "
                            class="pack28 text1"
                            >{{ item.title }}</span
                          >
                        </router-link>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-layout>
            </v-card>
          </v-flex>
        </v-layout>
        <!-- </v-img> -->
      </v-flex>
    </v-layout>

    <!-- For Small screen -->

    <v-layout class="hidden-md-and-up gradtop">
      <v-flex xs12>
        <!-- <v-img src="../../assets/Images/hd.jpg"> -->
        <v-layout wrap>
          <v-flex xs11 align-self-start>
            <!-- <router-link to="/" style="text-decoration: none"
                  > -->
            <v-layout wrap justify-start>
              <v-flex xs9  @click="$router.push('/')">
                <v-img
                  
                  contain
                  src="../assets/Images/logoorg.png"
                  width="200px"
                ></v-img>
              </v-flex>
            </v-layout>
            <!-- </router-link
                > -->
          </v-flex>
          <v-flex xs1 pt-5>
            <v-app-bar-nav-icon @click="nav = true">
              <v-icon color="White">mdi-menu</v-icon>
            </v-app-bar-nav-icon>
          </v-flex>
        </v-layout>
        <!-- </v-img> -->
      </v-flex>
    </v-layout>
    <v-navigation-drawer
      left
      v-model="nav"
      app
      fixed
      temporary
      style="background-color: #f7f7f7"
    >
      <v-layout wrap justify-center>
        <v-flex
          style="font-family: intersemib; font-size: 17px; text-align: justify"
        >
          <v-list dense nav>
            <v-list-item
              v-for="item in category"
              :key="item.title"
              link
              :to="item.route"
            >
              <v-list-item-icon>
                <v-img height="20px" contain :src="item.src"></v-img>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title
                  ><span style="font-color: black" class="fnt1">{{
                    item.title
                  }}</span></v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-flex>
      </v-layout>
    </v-navigation-drawer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      nav: false,
      items: [
        { title: "Home", route: "/", type: "link" },
        {
          title: "About Us",
          route: "/AboutusPage",
          type: "link",
        },
        { title: "Courses", route: "/CoursesPage", type: "link" },

        { title: "Gallery", route: "/GalleryPage", type: "link" },
        { title: "Contact Us", route: "/ContactusPage" },
      ],
      category: [
        { title: "Home", route: "/", type: "link" },
        {
          title: "About Us",
          route: "/AboutusPage",
          type: "link",
          path: "#about",
        },
        { title: "Courses", route: "/CoursesPage", type: "link" },
        { title: "Gallery", route: "/GalleryPage", type: "link" },
        { title: "Contact Us", route: "/ContactusPage" },
      ],
    };
  },
};
</script>
<style>
.router-link {
  text-decoration: none;
}
.navbar {
  overflow: hidden;
  background-color: #333;
  position: fixed;
  top: 0;
  width: 100%;
  height: 100%;
}
.fixItem {
  position: -webkit-sticky;
  position: sticky;
  top: 0px;
  z-index: 1;
  /* overflow: hidden;
      position: relative;
      height: 100%; */
}
.fnt1 {
  font-size: 13px;
  font-weight: bold;
}

.app-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 120px;
  height: 64px; /* adjust to desired height */
  background-color: #fff; /* adjust to desired background color */
  border-bottom: 1px solid #ccc; /* adjust to desired border style */
  z-index: 999; /* adjust to desired z-index */
}

.app-content {
  margin-top: 64px; /* adjust to match app bar height */
}

.gradtop {
  /* background-image:inear-gradient(255.36deg, #7BC142 48.09%, #E95D49 127.63%) ; */
  background-image: linear-gradient(#f7f7f7, #f7f7f7);
}
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 70px; /* adjust height as needed */
  background-color: #fff; /* adjust background color as needed */
  border-bottom: 1px solid #ccc; /* add a border if needed */
  z-index: 999; /* adjust z-index as needed */
}
.container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: auto;
}
</style>
