import { Component } from '@angular/core';
import { PRODUCTS } from '../../data/products';
import { Product } from '../../models/product.model';

@Component ({
    selector: 'app-product-list',
    standalone: true,
    templateUrl: './product-list.component.html',
    styleUrl: './product-list.component.css',
})

export class ProductListComponent {
    products: Product[] = PRODUCTS;

    stars(rating: number): string[] {
        const filled = Math.round(rating);
        const result: string[] = [];
        for(let i = 0; i < 5; i++){
            result.push(i < filled ? '★' : '☆');
        }
        return result;
    }
    whatsappLink(p: Product): string {
        const msg = `Check this product on whatsapp: ${p.link}`;
        return `https://wa.me/?text=${encodeURIComponent(msg)}`;
    }

    telegramLink(p: Product): string {
        const msg = `Check this product on telegram: ${p.link}`;
        return `https://t.me/share/url?url=${encodeURIComponent(p.link)}&text=${encodeURIComponent(p.name)}`;
    }

    likeProduct(p: Product) {
        p.likes++;
    }

    deleteProduct(p: Product) {
        this.products = this.products.filter(x => x.id !== p.id);
    }
    selectedCategory: string = 'all';

    setCategory(c: string) {
        this.selectedCategory = c;
    }

    get filteredProducts(): Product[] {
        if (this.selectedCategory === 'all') return this.products;
        return this.products.filter(p => p.category === this.selectedCategory);
    }
}






