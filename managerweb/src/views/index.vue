<template>
  <el-container>
    <el-aside :style=asideStyle>
<!--      <sidebar @fromSidebar="getFromSidebar"></sidebar>-->
      <sidebar/>
    </el-aside>
    <el-container>
      <el-header class="headerbar" style="height: 40px">
        <headerbar/>
      </el-header>
      <el-header class="breadcrumb" style="height: 30px">
        <breadcrumb/>
      </el-header>
      <el-main>
        <search></search>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
// import sidebar from '@/views/sidebar'
// import search from '@//views/sidebar/real/search'
const sidebar = () => import('@/views/sidebar')
const headerbar = () => import('@/views/headerbar')
const breadcrumb = () => import('@/views/breadcrumb')

const search = () => import('@//views/sidebar/real/search')

export default {
  components: {
    sidebar,
    headerbar,
    breadcrumb,
    search
  },
  data () {
    return {
      asideStyle: 'width: 12%;overflow:hidden;'
    }
  },
  methods: {
    // getFromSidebar (val) {
    //   if (val) {
    //     this.asideStyle = 'width: 64px;'
    //   } else {
    //     this.asideStyle = 'width: 12%;'
    //   }
    // }
  }
}
</script>

<style lang="scss">
  .el-header {
    /*background-color: #B3C0D1;*/
    color: #333;
    text-align: left;
    /*line-height: 60px;*/
  }

  .el-aside {
    background-color: #EFD37D;
    /*color: #333;*/
    text-align: left;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .headerbar {
    background-color: #ED630D;
    line-height: 40px;
  }

  .breadcrumb {
    line-height: 30px;
  }

  /*.el-container:nth-child(5) .el-aside,*/
  /*.el-container:nth-child(6) .el-aside {*/
  /*  line-height: 260px;*/
  /*}*/

  /*.el-container:nth-child(7) .el-aside {*/
  /*  line-height: 320px;*/
  /*}*/
</style>
