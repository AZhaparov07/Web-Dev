import { Injectable } from '@angular/core';
import { Album } from '../models/album.model';

export interface Photo {
  albumId: number;
  id: number;
  title: string;
  url: string;
  thumbnailUrl: string;
}

@Injectable({ providedIn: 'root' })
export class AlbumStoreService {
  // private storageKey = 'albums-data';
  private albumsData: Album[] = [
    { userId: 1, id: 1, title: 'quidem molestiae enim' },
    { userId: 1, id: 2, title: 'sunt qui excepturi placeat culpa' },
    { userId: 1, id: 3, title: 'omnis laborum odio' },
    { userId: 1, id: 4, title: 'non esse culpa molestiae omnis sed optio' },
    { userId: 1, id: 5, title: 'eaque aut omnis a' },
    { userId: 1, id: 6, title: 'natus impedit quibusdam illo est' },
    { userId: 1, id: 7, title: 'quibusdam autem aliquid et et quia' },
    { userId: 1, id: 8, title: 'qui fuga est a eum' },
    { userId: 1, id: 9, title: 'saepe unde necessitatibus rem' },
    { userId: 1, id: 10, title: 'distinctio laborum qui' },
    { userId: 1, id: 11, title: 'quam nostrum impedit mollitia quod et dolor' },
  ];

  private photosData: Photo[] = [];

constructor() {
  for (let albumId = 1; albumId <= 11; albumId++) {
    for (let i = 1; i <= 12; i++) {
      const id = albumId * 1000 + i; 
      this.photosData.push({
        albumId,
        id,
        title: `Album ${albumId} — photo ${i}`,
        url: `https://picsum.photos/seed/${id}/900/600`,
        thumbnailUrl: `https://picsum.photos/seed/${id}/260/180`,
      });
    }
  }
}
  getAlbums(): Album[] {
    return this.albumsData;
  }

  getAlbum(id: number): Album | undefined {
    return this.albumsData.find(a => a.id === id);
  }

  updateAlbumTitle(id: number, newTitle: string): void {
    const a = this.getAlbum(id);
    if (a) a.title = newTitle;
  }

  deleteAlbum(id: number): void {
    this.albumsData = this.albumsData.filter(a => a.id !== id);
    this.photosData = this.photosData.filter(p => p.albumId !== id);
  }

  getPhotosByAlbum(id: number): Photo[] {
    const list = this.photosData.filter(p => p.albumId === id);
    if (list.length > 0) return list;

    return [
      { albumId: id, id: 1000 + id * 10 + 1, title: 'default photo 1', url: 'https://picsum.photos/seed/a' + id + '1/600/400', thumbnailUrl: 'https://picsum.photos/seed/a' + id + '1/200/140' },
      { albumId: id, id: 1000 + id * 10 + 2, title: 'default photo 2', url: 'https://picsum.photos/seed/a' + id + '2/600/400', thumbnailUrl: 'https://picsum.photos/seed/a' + id + '2/200/140' },
      { albumId: id, id: 1000 + id * 10 + 3, title: 'default photo 3', url: 'https://picsum.photos/seed/a' + id + '3/600/400', thumbnailUrl: 'https://picsum.photos/seed/a' + id + '3/200/140' },
    ];
  }
}

