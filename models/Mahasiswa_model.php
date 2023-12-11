<?php
	/**
	 * 
	 */
	class Mahasiswa_model extends Controller
	{
		// private $mhs=[
		// 	[
		// 		"nama"=>"bayu",
		// 		"nrp"=>"123",
		// 		"email"=>"bayu.com",
		// 		"jurusan"=>"komputer"
		// 	],
		// 	[
		// 		"nama"=>"coki",
		// 		"nrp"=>"456",
		// 		"email"=>"coki.com",
		// 		"jurusan"=>"ekonomi"
		// 	],
		// 	[
		// 		"nama"=>"gempur",
		// 		"nrp"=>"789",
		// 		"email"=>"gempur.com",
		// 		"jurusan"=>"perawat"
		// 	]
		// ];

		private $table='mahasiswa';
		private $db;

		public function __construct()
		{
			$this->db=new database();
		}
		public function GetAllMahasiswa()
		{
			$this->db->query('SELECT * FROM '.$this->table);
			return $this->db->resultSet();
		}

		public function GetMahasiswaById($id)
		{
			$this->db->query('SELECT * FROM '.$this->table.' WHERE id=:id');
			$this->db->bind('id',$id);
			return $this->db->single();
		}

		public function tambahDataMahasiswa($data)
		{
			$query="INSERT INTO mahasiswa VALUES('',:nama,:nrp,:email,:jurusan)";
			$this->db->query($query);
			$this->db->bind('nama',$data['nama']);
			$this->db->bind('nrp',$data['nrp']);
			$this->db->bind('email',$data['email']);
			$this->db->bind('jurusan',$data['jurusan']);
			$this->db->execute();
			return $this->db->rowCount();
		}

		public function hapusDataMahasiswa($id)
		{
			$query="DELETE FROM mahasiswa WHERE id=:id";
			$this->db->query($query);
			$this->db->bind('id',$id);
			$this->db->execute();
			return $this->db->rowCount();
		}
	}