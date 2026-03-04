import { TestBed } from '@angular/core/testing';
import { AlbumsComponent } from './albums';

describe('AlbumsComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AlbumsComponent],
    }).compileComponents();
  });

  it('should create', () => {
    const fixture = TestBed.createComponent(AlbumsComponent);
    const component = fixture.componentInstance;
    expect(component).toBeTruthy();
  });
});