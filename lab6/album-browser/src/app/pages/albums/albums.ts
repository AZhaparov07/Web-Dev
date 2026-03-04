import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { Album } from '../../models/album.model';
import { AlbumStoreService } from '../../services/album-store.service';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './albums.html',
  styleUrl: './albums.css',
})
export class AlbumsComponent implements OnInit {
  loading = false;
  error = '';
  albums: Album[] = [];

  constructor(private router: Router, private store: AlbumStoreService) {}

  ngOnInit(): void {
    this.albums = this.store.getAlbums();
  }

  openAlbum(id: number): void {
    this.router.navigate(['/albums', id]);
  }

  deleteAlbum(id: number): void {
    this.store.deleteAlbum(id);
    this.albums = this.store.getAlbums(); 
  }
}