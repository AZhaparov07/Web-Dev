import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumStoreService, Photo } from '../../services/album-store.service';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './album-photos.html',
  styleUrl: './album-photos.css',
})
export class AlbumPhotosComponent implements OnInit {
  albumId = 0;
  photos: Photo[] = [];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private store: AlbumStoreService
  ) {}

  ngOnInit(): void {
    this.albumId = Number(this.route.snapshot.paramMap.get('id'));
    this.photos = this.store.getPhotosByAlbum(this.albumId);
  }

  back(): void {
    this.router.navigate(['/albums', this.albumId]);
  }
}