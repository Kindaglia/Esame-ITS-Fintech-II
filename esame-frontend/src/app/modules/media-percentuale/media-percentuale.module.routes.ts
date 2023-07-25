import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { MediaPercentualeComponent } from './media-percentuale.component';


const routes: any[] = [
    { path: 'media-percentuale', component: MediaPercentualeComponent }
];

@NgModule({
    exports: [
        RouterModule
    ]
})

export class MediaPercentualeRoutingModule {
    static forChild() {
        return RouterModule.forChild(
            routes
        )
    }
}