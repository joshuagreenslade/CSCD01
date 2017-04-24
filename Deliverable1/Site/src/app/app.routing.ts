import {ModuleWithProviders} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';

import {HomeComponent} from './components/home/home.component';
import {AboutComponent} from './components/about/about.component';
import {TeamComponent} from './components/team/team.component';
import {ProjectComponent} from './components/project/project.component';
import { MemberComponent } from './components/member/member.component';
import { DeliverableOneComponent } from './components/deliverables/deliverable-one/deliverable-one.component';



const appRoutes: Routes = [

    {
        path:'',
        component: HomeComponent
    },
    {
        path: 'about',
        component: AboutComponent
    },
    {
        path: 'team',
        component: TeamComponent
    },
    {
        path: 'team/:id',
        component: MemberComponent
    },
    {
        path: 'project',
        component: ProjectComponent
    },
    {
        path: 'project/one',
        component: DeliverableOneComponent
    },
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);