<template>
  <el-table v-loading="tableLoading" :data="tableData" style="width: 100%" :fit="true" border>
    <el-table-column label="状态" prop="power_status" align="center" width="100" />
    <el-table-column label="虚拟机名称" prop="vmname" align="center" width="240" />
    <el-table-column label="虚拟机IP" prop="ip_address" align="center" width="200" />
    <el-table-column label="宿主机" prop="hostname" align="center" width="200" />
    <el-table-column label="内存" prop="mem_size" align="center" width="100" />
    <el-table-column label="CPU" prop="num_vcpu" align="center" width="100" />
    <el-table-column label="总容量" prop="total_storage" align="center" width="120" />
    <el-table-column label="已使用容量" prop="used_storage" align="center" width="120" />
    <el-table-column label="备注" prop="description" align="center" :show-overflow-tooltip="true" />
    <el-table-column align="center" width="240">
      <template slot="header" slot-scope="">
        <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
      </template>
      <template slot-scope="scope">
        <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      tableData: [],
      tableLoading: true,
      search: ''
    }
  },
  mounted() {
    this.tableLoading = true
    axios
      .get(' http://localhost:3001/virtual')
      .then(res => {
        // console.log(res.data)
        this.tableData = res.data
        this.tableLoading = false
      })
      .catch(err => console.log(err))
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row)
    },
    handleDelete(index, row) {
      console.log(index, row)
    }
  }
}
</script>
