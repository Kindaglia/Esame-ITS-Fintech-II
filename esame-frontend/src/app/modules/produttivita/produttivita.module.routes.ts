import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ProduttivitaComponent } from './produttivita.component';
const routes: any[] = [
    { path: 'produttivita', component: ProduttivitaComponent }
];

@NgModule({
    exports: [
        RouterModule
    ]
})

export class ProduttivitaRoutingModule {
    static forChild() {
        return RouterModule.forChild(
            routes
        )
    }
}