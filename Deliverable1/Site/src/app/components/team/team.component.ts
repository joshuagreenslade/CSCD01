import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MembersService } from '../../services/members.service';

@Component({
  selector: 'app-team',
  templateUrl: './team.component.html',
  styleUrls: ['./team.component.css']
})
export class TeamComponent implements OnInit {

  keys: any[];
  members: {};

  constructor(private __memberService:MembersService) {}

  ngOnInit() {

    this.__memberService.getMembers()
      .subscribe(members => {
          this.keys = Object.keys(members.members);
          this.members = members.members;
        }
      );

      
  }

}
