import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Album } from '../../models/album.model';
import { AlbumStoreService } from '../../services/album-store.service';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './album-detail.html',
  styleUrl: './album-detail.css',
})
export class AlbumDetailComponent implements OnInit {
  loading = false;
  error = '';
  album: Album | null = null;
  titleValue = '';
  photoCount: number = 5;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private store: AlbumStoreService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    const found = this.store.getAlbum(id);

    if (!found) {
      this.error = 'Album not found';
      return;
    }

    this.album = found;
    this.titleValue = found.title;
  }

  save(): void {
    if (!this.album) return;

    this.store.updateAlbumTitle(this.album.id, this.titleValue);

    this.album.title = this.titleValue;
  }

  viewPhotos(): void {
    if (!this.album) return;
    this.router.navigate(['/albums', this.album.id, 'photos']);
  }

  back(): void {
    this.router.navigate(['/albums']);
  }
}